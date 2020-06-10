# TODOS

## General

- figure out how to share options between Click commands
- `--logfile` option should create CSV of simplified representation of responses, with metafields of `logged_at`, `error_code` 
- Create a log file format to allow easy appending, e.g.

    ```
    ## TWITKIT-LOG timestamp-command
    logged_at,error_code,id,text
    etc,etc,etc,etc
    ## /TWITKIT-LOG timestamp-command
    ```


## SimpleDatum class

- Simplifed, flattened dict representation for User and Tweet
- Can be constructed from a Tweepy.models.Model
- Can be constructed from dict (for easy testing purposes)
- Acts like a read only dict
- has logged_at attribute upon creation
