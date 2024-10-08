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

obj = APIBase("torch.any")


def test_case_1():
    pytorch_code = textwrap.dedent(
        """
        import torch
        a = torch.rand(1, 2).bool()
        result = torch.any(a)
        """
    )
    obj.run(pytorch_code, ["result"])


def test_case_2():
    pytorch_code = textwrap.dedent(
        """
        import torch
        a = torch.rand(3, 4)
        result = torch.any(a)
        """
    )
    obj.run(pytorch_code, ["result"])


def test_case_3():
    pytorch_code = textwrap.dedent(
        """
        import torch
        a = torch.rand(4, 3)
        result = torch.any(a, 1)
        """
    )
    obj.run(pytorch_code, ["result"])


def test_case_4():
    pytorch_code = textwrap.dedent(
        """
        import torch
        a = torch.rand(4, 3)
        result = torch.any(a, 1, True)
        """
    )
    obj.run(pytorch_code, ["result"])


def test_case_5():
    pytorch_code = textwrap.dedent(
        """
        import torch
        a = torch.rand(4, 3)
        result = torch.any(a, dim=0, keepdim=False)
        """
    )
    obj.run(pytorch_code, ["result"])


def test_case_6():
    pytorch_code = textwrap.dedent(
        """
        import torch
        a = torch.tensor([False, False, False])
        torch.any(torch.tensor([[4, 0, 7], [0, 2, 6]]), dim=0, keepdim=False, out=a)
        """
    )
    obj.run(pytorch_code, ["a"])


def test_case_7():
    pytorch_code = textwrap.dedent(
        """
        import torch
        a = torch.tensor([False, False, False])
        torch.any(input=torch.tensor([[4, 0, 7], [0, 2, 6]]), dim=0, keepdim=False, out=a)
        """
    )
    obj.run(pytorch_code, ["a"])


def test_case_8():
    pytorch_code = textwrap.dedent(
        """
        import torch
        a = torch.tensor([False, False, False])
        torch.any(keepdim=False, dim=0, out=a, input=torch.tensor([[4, 0, 7], [0, 2, 6]]))
        """
    )
    obj.run(pytorch_code, ["a"])


def test_case_9():
    pytorch_code = textwrap.dedent(
        """
        import torch
        a = torch.tensor([[4, 0, 7], [0, 2, 6]], dtype=torch.int32)
        result = torch.any(a)
        """
    )
    obj.run(pytorch_code, ["result"])


def test_case_10():
    pytorch_code = textwrap.dedent(
        """
        import torch
        a = torch.tensor([[4, 0, 7], [0, 2, 6]], dtype=torch.int64)
        result = torch.any(a, 1)
        """
    )
    obj.run(pytorch_code, ["result"])


def test_case_11():
    pytorch_code = textwrap.dedent(
        """
        import torch
        a = torch.tensor([[4, 0, 7], [0, 2, 6]], dtype=torch.float64)
        result = torch.any(a, 1, True)
        """
    )
    obj.run(pytorch_code, ["result"])


def test_case_12():
    pytorch_code = textwrap.dedent(
        """
        import torch
        a = torch.tensor([[4, 0, 7], [0, 2, 6]], dtype=torch.float32)
        result = torch.any(a, dim=0, keepdim=False)
        """
    )
    obj.run(pytorch_code, ["result"])
