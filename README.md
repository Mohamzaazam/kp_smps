winget install -e --id ImageMagick.ImageMagick
winget install -e --id Google.Libwebp
winget install -e --id Inkscape.Inkscape

# restart vscode and then do this

VS Code terminal still blind?

Fully quit VS Code (it caches PATH), then relaunch. If needed, re-hydrate PATH inside that terminal:

$env:Path = [Environment]::GetEnvironmentVariable('Path','Machine') + ';' +
            [Environment]::GetEnvironmentVariable('Path','User')


(VS Code terminals often need a restart to pick up PATH changes.


Use the console Inkscape binary

On Windows, inkscape.com is the console app; inkscape.exe is GUI (prints nothing). In POSIX shells, call:

/c/Program\ Files/Inkscape/bin/inkscape.com --version


If you want inkscape to work, add an alias in ~/.bashrc:

alias inkscape='/c/Program\ Files/Inkscape/bin/inkscape.com'


magick -version
magick -list format | grep -i "WEBP\|SVG"   # use 'findstr /I "WEBP SVG"' on cmd/PowerShell
cwebp -version
inkscape --version
