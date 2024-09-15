import urllib.request
from threading import Thread

class CustomThread(Thread):
    def __init__(self, url, filename, url1 , filename1):
        super().__init__()
        self.filename = filename

    def run(self):
        # create a thread
        print("DOWNLOADING....")
        urllib.request.urlretrieve(self.url, self.filename)
        print("downloaded successfully")


def main():
    url1 = "https://en.wikipedia.org/wiki/British_logistics_in_the_Normandy_campaign"
    url2 = "https://en.wikipedia.org/wiki/States_and_union_territories_of_India"
    filename1 = "downloaded_file1.html"
    filename2 = "downloaded_file2.html"

    thread1 = CustomThread(url1, filename1)
    print("----MAIN THREAD---- : CREATING A NEW ONE")
    thread2 = CustomThread(url2, filename2)
    print("----MAIN THREAD---- : CREATING A NEW ONE")

    thread1.start()
    thread2.start()
    print("-----WAITING FOR FINISHING---------")

    thread1.join()
    thread2.join()
    print("-----MAIN THREAD----: DONE")

if __name__ == "__main__":
    main()
