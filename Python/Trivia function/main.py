import requests
def main():
    print("Hello learners!")
    n=int(input("Enter a number:"))
    trivia=trivia_fetch(n)
    print(f"The trivia for entered number,{n} is {trivia['text']}")
def trivia_fetch(num):
    response=requests.get(f'http://numbersapi.com/{num}?json')
    return response.json()
if __name__=="__main__":
  main()