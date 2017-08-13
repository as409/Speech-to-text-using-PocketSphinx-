# Speech-to-text-using-PocketSphinx-
Text conversion of a live stream as well as an input file
## Setup and dependencies :
- install Sphinxbase and PocketSphinx 
- Place your training models in the model folder 

To directly run it from command line use the command : pocketsphinx_continuous -infile myfile.wav 

The input file should be a 16khz 16 bit mono .wav file

you can convert a mp3 file using the command : ffmpeg -i yourfile.mp3 -acodec pcm_s16le -ac 1 -ar 16000 myfile.wav



###PocketSphinx -

####Input - Mr Bean drinks 8 cups of coffee a day.Mrs Bean thinks that Mr Bean drinks too much coffee.Mr Bean asked How many cups of coffee do you normally drink? Mrs Bean replied, I only drink 2 cups of coffee a day. Mr Bean promised not to drink so much coffee in the future.

####Output - mr bean drinks eight cups of coffee a day the sistine thinks that mr bean drinks too much coffee this could be an oscar how many cups of coffee do you normally drink mrs dean replied i barely drink two cups of coffee a day mr bean must not to drink so much coffee in the future

Using the *tensorflow's* sppech to text  https://github.com/buriburisuri/speech-to-text-wavenet 

 
####Input - Mr Bean drinks 8 cups of coffee a day.Mrs Bean thinks that Mr Bean drinks too much coffee.Mr Bean asked How many cups of coffee do you normally drink? Mrs Bean replied, I only drink 2 cups of coffee a day. Mr Bean promised not to drink so much coffee in the future.

####Output - missr ben grings eaght cups of coffey a day missus being tink that mistrbein trinks to much caoffe mistr ben aske how an y cups of coffe to you normoly dring missus be rylied i a medring to cups of coffee a dhey mis e ben promised not to drink  sa much couffee in the futur


Note- Both the machines are not trained and are running on the prebuilt models
