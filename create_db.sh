#!/bin/sh

CREATE_TABLE_SQL='create table debit1(hash char(64), card_no char(16), type varchar(10), date char(8), amount real, desc varchar(256));'
sqlite3 transaction_records.db <<< $CREATE_TABLE_SQL
