# python_autosync
a python app that uses uploader premium to sync files in a folder to a remote source

basically it uses the uploader-premium's inbuilt API to not just upload files but to sync them accross the remote and local sources.

## Requirements
**required setup**
**Python**
this was written using **python 3.12.6**. so go nuts. if you dont know how to install it then do us both a favor and ask an LLM how. Also if you still havent installed python on your system then this project wont help you *just being honest here*

**required packages**
1. **watchdog**  
this is kinda the MC in this anime, without it the rest will work but wont have any direction

```bash
	pip install watchdog
```
2. **Requests**  
this handles sending requests to the uploader API

```bash
	pip install requests
```
3. **asyncio**  
this enables python code to run synchronously to prevent the uploading to block any concurrent activity like mass updating of files

```bash
	pip install asyncio
```

**basics**
1. **Must know python**  
at least enough not to fuck everything up
2. **Must update to the latest version when available**  
since this is basically 2 of my babies interacting you need to update both this and its companion `uploader-premium` whenever i update either
3. **Have fun, but not too much**  
Feel free to make your own changes and submit a pull request whenever you feel like you've added something worth updating to the project. but dont make changes so big that it will be impossible for my brain to read and understand. im an actual human btw

## how to use
- clone the repo
- run `main.py`
- give the details
- enjoy

## Note
please note that:
- it requires an uploader-premium API key to use. (ill give the steps to getting it once ive set it up)
- its not perfect there are alot of opportunities to break the whole system
- requires that you've set up uploader premium somewhere
- its a work in progress so dont expect it to be perfect right out of the box
