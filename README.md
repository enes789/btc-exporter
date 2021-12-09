# Bitcoin node exporter

## QuickStart

```
docker-compose up -d
```

Btc node exporter will give you two metrics;

# HELP bitcoin_balance The total balance of prod bitcoin wallet.
# TYPE bitcoin_balance gauge
bitcoin_balance 0.000001
# HELP bitcoin_block_number The block number of bitcoin.
# TYPE bitcoin_block_number gauge
bitcoin_block_number 713359.0

You can custome app.py file to add more metrics





