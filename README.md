## Some screenshots:

<img width="1402" height="621" alt="image" src="https://github.com/user-attachments/assets/122231e8-15a5-4b54-b71f-c9b1f22c8c57" />

<img width="892" height="482" alt="image" src="https://github.com/user-attachments/assets/201bd958-a5fe-4d17-b92b-18820f87ff73" />

<img width="981" height="129" alt="image" src="https://github.com/user-attachments/assets/e1cbc56e-5d58-41c2-8606-23d07f65633c" />

(Had to change the model because of this 503 error)
<img width="868" height="296" alt="image" src="https://github.com/user-attachments/assets/1c9ef4f9-8f2a-423f-a58b-f332ace7eee4" />

gemini-3.1-flash-lite worked

## Instructions

 - Replace "gemini-3.5-flask" with "gemini-3.1-flash-lite" in the base.py file in agents folder if you encounter the same issue
 
 - Also, make sure to create an api key and add it to a .env file as GOOGLE_API_KEY = <your api key> or GEMINI_API_KEY = <Your api key> 
 
 - Use ```adk web .``` on your terminal to run this project in the web, instead of the regular python run command.

 - Here is the prompt example used in the screenshot, you can use it to test the agents (It mimics the deployment errors thrown on vercel):
 ```
[INFO] Starting build... 

[INFO] pip install -r requirements.txt 

[ERROR] Could not find a version that satisfies the requirement tensorflew==2.14.0 (from versions: none) 

[ERROR] No matching distribution found for tensorflew==2.14.0 

[FATAL] Build aborted due to step failure.
```
