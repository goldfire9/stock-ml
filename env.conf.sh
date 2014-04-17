if [ -z "$_STOCK_ML_ENV_CONF_H_" ]; then
	declare -xr _STOCK_ML_ENV_CONF_H_="true"
    #__RELEASE__=true

	declare -xr DATA_DIR="$HOME/data/stock"
	declare -xr DUMP_DIR="$HOME/dump/quant/stock-ml"
	declare -xr LOG_DIR="$HOME/log/quant/stock-ml"
    declare -xr INC_DIR="$HOME/code/inc"

    if [ -n "$__RELEASE__" ]; then
        [ ! -e $DUMP_DIR ] && mkdir -pv $DUMP_DIR
        [ ! -e $LOG_DIR ] && mkdir -pv $LOG_DIR
    fi
    echo "Environment setup finished in $(pwd)"
fi
