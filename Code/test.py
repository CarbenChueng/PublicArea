import torch
import torch.backends.mps as mps
from _PythonProject.DigitalRecognition.net import Net

# a = torch.tensor([[0., 0., 0., 0., 1., 0., 0., 0., 0., 0.],
#             [1., 0., 0., 0., 0., 0., 0., 0., 0., 0.]])
# b = torch.tensor([[0.0992, 0.0864, 0.1013, 0.1054, 0.0991, 0.1001, 0.1009, 0.1105, 0.0973,
#              0.0997],
#             [0.1001, 0.0892, 0.1025, 0.0997, 0.0970, 0.0994, 0.1068, 0.1089, 0.1009,
#              0.0954]])
# print(torch.argmax(a,dim=1))
# print(mps.is_available())
model = Net()
model.load_state_dict(torch.load("/Users/carbenchueng/Desktop/1-Git/Code/_PythonProject/DigitalRecognition/prarm/0.pt"))

input_tc = torch.randn((1,784))
traced_script_model = torch.jit.trace(model,input_tc)
traced_script_model.save("mnist.pt")
