# python code to search in YouTube using api

first download googleapiclient library you can use this command

    >  pip install -r  requirements.txt 

include from googleapiclient.discovery the build function 

include config file to use the key, to use the key you can call this `config.key` which contain key value

call the function `Search`
you need to pass to the pervious function :

   1. key
   2. keyword
   3. number of result you wont to receive
   4. order to filter the result
   5. type to get videos or channels or playlists

if everything working fine you will receive the result in list of dictionaries 

you can get the name value by using the key `'name'`

and the URL value by using the key `'url'`
