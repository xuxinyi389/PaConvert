# Copyright (c) 2023 PaddlePaddle Authors. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import textwrap

from apibase import APIBase

obj = APIBase("torch.nn.ConvTranspose1d")


def test_case_1():
    pytorch_code = textwrap.dedent(
        """
        import torch
        import torch.nn as nn
        x = torch.randn(20, 16, 50)
        model = nn.ConvTranspose1d(16, 33, 3, stride=2, bias=False)
        result = model(x)
        """
    )
    obj.run(pytorch_code, ["result"], check_value=False)


def test_case_2():
    pytorch_code = textwrap.dedent(
        """
        import torch
        import torch.nn as nn
        x = torch.randn(20, 16, 50)
        model = nn.ConvTranspose1d(16, 33, 3, stride=2, padding=4, bias=False)
        result = model(x)
        """
    )
    obj.run(pytorch_code, ["result"], check_value=False)


def test_case_3():
    pytorch_code = textwrap.dedent(
        """
        import torch
        import torch.nn as nn
        x = torch.randn(20, 16, 50)
        model = nn.ConvTranspose1d(16, 33,  5, stride=2, padding=2, dilation=1, bias=False)
        result = model(x)
        """
    )
    obj.run(pytorch_code, ["result"], check_value=False)


def test_case_4():
    pytorch_code = textwrap.dedent(
        """
        import torch
        import torch.nn as nn
        x = torch.randn(5, 16, 50)
        model = nn.ConvTranspose1d(16, 33, 5, stride=1, padding=4, dilation=3, bias=True)
        result = model(x)
        """
    )
    obj.run(pytorch_code, ["result"], check_value=False)


def test_case_5():
    pytorch_code = textwrap.dedent(
        """
        import torch
        import torch.nn as nn

        x = torch.randn(5, 16, 50)
        model = nn.ConvTranspose1d(in_channels=16, out_channels=33, kernel_size=5, stride=1, padding=4, output_padding=0, groups=1, bias=True, dilation=3,
                                   padding_mode='zeros', device=None, dtype=None)
        result = model(x)
        """
    )
    obj.run(
        pytorch_code,
        ["result"],
        unsupport=True,
        reason="Paddle does not support parameter of padding_mode",
    )


def test_case_6():
    pytorch_code = textwrap.dedent(
        """
        import torch
        import torch.nn as nn

        x = torch.randn(5, 16, 50)
        model = nn.ConvTranspose1d(in_channels=16, kernel_size=5, out_channels=33, stride=1, padding=4, device=None, groups=1, bias=True, output_padding=0, dilation=3,
                                   padding_mode='zeros', dtype=None)
        result = model(x)
        """
    )
    obj.run(
        pytorch_code,
        ["result"],
        unsupport=True,
        reason="Paddle does not support parameter of padding_mode",
    )


def test_case_7():
    pytorch_code = textwrap.dedent(
        """
        import torch
        import torch.nn as nn

        x = torch.randn(5, 16, 50)
        model = nn.ConvTranspose1d(16, 33, 5, 1, 4, 0, 1, True, 3, 'zeros', None, None)
        result = model(x)
        """
    )
    obj.run(
        pytorch_code,
        ["result"],
        unsupport=True,
        reason="Paddle does not support parameter of padding_mode",
    )


def test_case_8():
    pytorch_code = textwrap.dedent(
        """
        import torch
        import torch.nn as nn

        x = torch.randn(5, 16, 50)
        model = nn.ConvTranspose1d(16, 33, 5)
        result = model(x)
        """
    )
    obj.run(pytorch_code, ["result"], check_value=False)
