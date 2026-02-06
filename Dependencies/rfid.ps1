

# Start the bot hidden using pythonw.exe
Start-Process python -ArgumentList "-m bot" -WindowStyle Hidden

# Start ngrok hidden
Start-Process ngrok -ArgumentList "http 8080" -WindowStyle Hidden
