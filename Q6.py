a=[{'name': 'affirm', 'confidence': 0.9448149204254},
  {'name': 'affirm', 'confidence': 0.944814920425415}, 
  {'name': 'inform', 'confidence': 0.9842240810394287},
  {'name': 'inform', 'confidence': 0.9842240810394287}]

b = {x['confidence']:x for x in a}.values()
print(b)