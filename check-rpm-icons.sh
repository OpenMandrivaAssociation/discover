#!/bin/bash
# Spot-check whether packages ship icons that createmd / Discover can use.
# Usage: ./check-rpm-icons.sh [pkgname ...]
# If no args, checks a default list of apps reported missing icons in Discover.

set -euo pipefail

pkgs=("$@")
if [ ${#pkgs[@]} -eq 0 ]; then
  pkgs=(
    delaboratory ephoto eruler fotocx frogr fritzing dust3d gpaint
    gnuplot gexif pixelize texmaker coolreader3 imv
    paperwork-gtk paperwork nfoview gimagereader
    lumina-screenshot lumina-image-viewer manslide
    white-dune xdvi alfspdfviewer kdbg abe abuse_sdl
  )
fi

check_pkg() {
  local p=$1
  local files=""
  if rpm -q "$p" &>/dev/null; then
    files=$(rpm -ql "$p" 2>/dev/null || true)
    echo "===== INSTALLED: $p ($(rpm -q "$p")) ====="
  else
    local rpmfile
    rpmfile=$(find /var/cache/libdnf5 /var/cache/dnf /home/bero -name "${p}-*.rpm" 2>/dev/null | head -1 || true)
    if [ -z "${rpmfile:-}" ]; then
      # Try downloading to temp (needs network + dnf5)
      local tmp
      tmp=$(mktemp -d)
      if dnf5 download -q --destdir="$tmp" "$p" 2>/dev/null; then
        rpmfile=$(find "$tmp" -name '*.rpm' | head -1)
      fi
      if [ -n "${rpmfile:-}" ] && [ -f "$rpmfile" ]; then
        files=$(rpm -qlp "$rpmfile" 2>/dev/null || true)
        echo "===== DOWNLOADED: $p ($rpmfile) ====="
        # leave temp for inspection; comment next line to keep
        rm -rf "$tmp"
      else
        rm -rf "$tmp"
        echo "===== NOT FOUND: $p ====="
        return
      fi
    else
      files=$(rpm -qlp "$rpmfile" 2>/dev/null || true)
      echo "===== CACHE: $p ($rpmfile) ====="
    fi
  fi

  local desktops icons_meta icons_pix icons_other
  desktops=$(echo "$files" | grep -E '/usr/share/applications/.*\.desktop$' || true)
  icons_meta=$(echo "$files" | grep -E '/usr/share/(icons|pixmaps)/' || true)
  icons_other=$(echo "$files" | grep -iE '\.(png|svg|svgz|xpm)$' | grep -vE '/usr/share/(icons|pixmaps)/' | head -20 || true)

  echo "-- desktop files --"
  if [ -z "$desktops" ]; then
    echo "(none)"
  else
    echo "$desktops"
    # If installed, show Icon=
    if rpm -q "$p" &>/dev/null; then
      while IFS= read -r d; do
        [ -f "$d" ] || continue
        echo "   Icon= from $d: $(grep -E '^Icon=' "$d" | head -1 || echo '(no Icon=)')"
      done <<< "$desktops"
    fi
  fi

  echo "-- icons under icons/ or pixmaps/ --"
  if [ -z "$icons_meta" ]; then
    echo "(none)"
  else
    echo "$icons_meta" | head -40
    local n
    n=$(echo "$icons_meta" | wc -l)
    [ "$n" -gt 40 ] && echo "... ($n total)"
  fi

  echo "-- other image files (sample) --"
  if [ -z "$icons_other" ]; then
    echo "(none)"
  else
    echo "$icons_other"
  fi

  # Catalog status if present
  if [ -d /var/cache/swcatalog/xml ]; then
    echo "-- catalog icon tags (swcatalog) --"
    if grep -R -l "<pkgname>$p</pkgname>" /var/cache/swcatalog/xml 2>/dev/null | head -1 | while read -r xml; do
      # extract component block roughly
      awk -v pkg="$p" '
        /<component/ { buf=""; keep=0 }
        { buf = buf $0 "\n" }
        /<\/component>/ {
          if (buf ~ "<pkgname>" pkg "</pkgname>") {
            while (match(buf, /<icon[^>]*>[^<]*<\/icon>/)) {
              print substr(buf, RSTART, RLENGTH)
              buf = substr(buf, RSTART+RLENGTH)
            }
            if (buf !~ /<icon/) print "(no <icon> tags in catalog for this pkgname)"
          }
        }
      ' "$xml"
    done | head -20; then
      :
    else
      echo "(pkgname not found in /var/cache/swcatalog/xml)"
    fi
  fi
  echo
}

for p in "${pkgs[@]}"; do
  check_pkg "$p"
done
