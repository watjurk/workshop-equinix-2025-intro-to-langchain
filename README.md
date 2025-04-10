#  Zero to hero: Introduction to LangChain
This file serves as a guide to our repository designed to help you get started as quickly as possible.

#  Dependency installation
We use pixi to install all dependencies quickly and effortlessly. You can find the installation guide on this website: https://pixi.sh/latest (don't worry, it is just a single line that you need to copy-paste into the terminal)

1. Open a new terminal window
2. Copy-paste the OS-specific installation line from  https://pixi.sh/latest into your terminal
3. Restart your terminal (PC if reopening the terminal results in pixi not recognized error)
4. Your environment should be ready to go!

#  Get a free API key from groqcloud
1. Open this link: https://console.groq.com/home 
2. Create an account / log in with google
3. Open the email you recieve and confirm your email address  
4. Go back to the website, and click on "Create API key"
5. In the repository, create a `.env` file in /src, so the resulting path will be `/src/.env`. This file is used to store variables securely. 
6. Open `.env`, and add this line: `GROQ_API_KEY=<Your_api_key_from_the_website>`
7. Run `pixi run start`

