import fire

def hello(name="World"):
  return "Hello %s From Mehran Shoshooghi!" % name

if __name__ == '__main__':
  fire.Fire(hello)
