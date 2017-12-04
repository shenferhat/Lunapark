# Lunapark
Get safe, fast and free of charge data from your remote PostgreSQL server as JSON.

## What does Lunapark do?
* mainClient sends your AES encrypted query to a public MQTT broker
* mainServer reads your message and decrypts it, executes your query
* mainServer encrypts the result JSON and sends it back to answer channel
* ???
* Profit

### Used Tech's
* MQTT Broker - Client
* PostgreSQL
* JSON
* AES Encryption


## Author

* **Şen Ferhat**

```
Android version for remote client soon
```

