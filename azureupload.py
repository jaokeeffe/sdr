#!/usr/bin/python

import azure.storage as azs
account = azs.CloudStorageAccount(account_name='hyperfineml',account_key='KQBYI5jV0nPinp/uheXZzqtdrGPKfoRGOoRsssPiLQxa/M+mvogXAf10SBEa8YuIbtMfly33nNXTtmISJoH3vg==')

service = account.create_block_blob_service()
service.create_blob_from_path('zipped','iq.txt.bz2','./iq.txt.bz2')
