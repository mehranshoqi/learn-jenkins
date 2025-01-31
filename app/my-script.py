import fire

def hello(name="World"):
  return "Hello %s From Mehran Shoshooghi 33!" % name

if __name__ == '__main__':
  fire.Fire(hello)
