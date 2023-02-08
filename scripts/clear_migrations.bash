# Ukavwe Israel - 08/06/2022
# run bash clear_migrations.bash (on linux and mac or use powershell for windows users)

#!/bin/bash

set -o errexit
set -o pipefail
set -o nounset

find ../src -path "*/migrations/*.py" -not -name "__init__.py" -delete
find ../src -path "*/migrations/__pycache__" -delete
find ../src -path "*/__pycache__" -delete
