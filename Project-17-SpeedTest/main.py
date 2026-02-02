import speedtest 
test = speedtest.Speedtest()
print("Searching for server...")
test.get_best_server()
print("Measuring download speed...")
download_speed = test.download()
print("Measuring upload speed...")
upload_speed = test.upload()
ping = test.results.ping
print(f'''Your connection speed: 
        Download Speed: {(download_speed/1024/1024):.2f} Mbps
        Upload Speed: {(upload_speed/1024/1024):.2f} Mbps
        Ping : {ping} ms
''')
