# AI Agent

Overview
This project is an AI-powered web browsing agent that automates interactions with YouTube. Using Google's Gemini 1.5 Flash model and the LangChain framework, the agent can navigate to YouTube, perform searches, and interact with video content autonomously.

# Features

Automated YouTube Navigation: Navigates directly to YouTube
Intelligent Search: Searches for specific video content
Content Interaction: Identifies and plays videos matching search criteria
Browser Automation: Controls web browser functionality through AI


# Requirements

Python 3.7+
Google API key with access to Gemini models




# Customization
You can customize the agent's behavior by modifying the task parameter. Examples:
python# Search for different content

task = 
          
  """ 
     Open YouTube and find the official channel of a news organization.
     Get the subscriber count and list the 3 most recent videos. """

       
# Perform different actions

task = """
      Open YouTube and find the official channel of a news organization.
      Get the subscriber count and list the 3 most recent videos.
"""
# How It Works

The agent initializes with the Gemini 1.5 Flash model
It interprets the task description in natural language
The browser automation system opens a web browser
The agent performs the necessary actions to complete the task
Results are returned through the run() method

# Troubleshooting

API Key Issues: Ensure your Google API key has access to Gemini models
Browser Access: The agent needs permission to launch and control a web browser
Task Clarity: For best results, provide clear and specific instructions in the task

# License
MIT License

# Acknowledgments

LangChain for the LLM framework
Google Gemini for the generative AI model
Browser-use for browser automation capabilities
