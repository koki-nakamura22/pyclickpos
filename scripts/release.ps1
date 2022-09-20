# Cleanup the previous released directories.
Remove-Item -Path .\build -Recurse -Force
Remove-Item -Path .\dist -Recurse -Force
Remove-Item -Path .\pyclickpos.egg-info -Recurse -Force

# Build then release
python setup.py sdist
python setup.py bdist_wheel
twine upload --repository pypi dist\*
