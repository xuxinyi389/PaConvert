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

obj = APIBase("torch.nn.functional.grid_sample")


def test_case_1():
    pytorch_code = textwrap.dedent(
        """
        import torch
        import torch.nn.functional as F
        x = torch.tensor([[[[-0.6,  0.8, -0.5], [-0.5,  0.2,  1.2], [ 1.4,  0.3, -0.2]]]])
        grid = torch.tensor([[[[ 0.2,  0.3],[-0.4, -0.3],[-0.9,  0.3],[-0.9, -0.6]],
                            [[ 0.4,  0.1],[ 0.9, -0.8],[ 0.4,  0.5],[ 0.5, -0.2]],
                            [[ 0.1, -0.8],[-0.3, -1. ],[ 0.7,  0.4],[ 0.2,  0.8]]]])
        result = F.grid_sample(x, grid)
        """
    )
    obj.run(pytorch_code, ["result"], check_value=False, check_stop_gradient=False)


def test_case_2():
    pytorch_code = textwrap.dedent(
        """
        import torch
        import torch.nn.functional as F
        x = torch.tensor([[[[-0.6,  0.8, -0.5], [-0.5,  0.2,  1.2], [ 1.4,  0.3, -0.2]]]])
        grid = torch.tensor([[[[ 0.2,  0.3],[-0.4, -0.3],[-0.9,  0.3],[-0.9, -0.6]],
                            [[ 0.4,  0.1],[ 0.9, -0.8],[ 0.4,  0.5],[ 0.5, -0.2]],
                            [[ 0.1, -0.8],[-0.3, -1. ],[ 0.7,  0.4],[ 0.2,  0.8]]]])
        result = F.grid_sample(x, grid, padding_mode="border")
        """
    )
    obj.run(pytorch_code, ["result"], check_value=False)


def test_case_3():
    pytorch_code = textwrap.dedent(
        """
        import torch
        import torch.nn.functional as F
        x = torch.tensor([[[[-0.6,  0.8, -0.5], [-0.5,  0.2,  1.2], [ 1.4,  0.3, -0.2]]]])
        grid = torch.tensor([[[[ 0.2,  0.3],[-0.4, -0.3],[-0.9,  0.3],[-0.9, -0.6]],
                            [[ 0.4,  0.1],[ 0.9, -0.8],[ 0.4,  0.5],[ 0.5, -0.2]],
                            [[ 0.1, -0.8],[-0.3, -1. ],[ 0.7,  0.4],[ 0.2,  0.8]]]])
        result = F.grid_sample(x, grid, mode='nearest')
        """
    )
    obj.run(pytorch_code, ["result"], check_value=False)


def test_case_4():
    pytorch_code = textwrap.dedent(
        """
        import torch
        import torch.nn.functional as F
        x = torch.tensor([[[[-0.6,  0.8, -0.5], [-0.5,  0.2,  1.2], [ 1.4,  0.3, -0.2]]]])
        grid = torch.tensor([[[[ 0.2,  0.3],[-0.4, -0.3],[-0.9,  0.3],[-0.9, -0.6]],
                            [[ 0.4,  0.1],[ 0.9, -0.8],[ 0.4,  0.5],[ 0.5, -0.2]],
                            [[ 0.1, -0.8],[-0.3, -1. ],[ 0.7,  0.4],[ 0.2,  0.8]]]])
        result = F.grid_sample(x, grid, mode='bilinear', align_corners=True)
        """
    )
    obj.run(pytorch_code, ["result"], check_value=False, check_stop_gradient=False)


def test_case_5():
    pytorch_code = textwrap.dedent(
        """
        import torch
        import torch.nn.functional as F
        x = torch.tensor([[[[[-0.6,  0.8, -0.5], [-0.5,  0.2,  1.2], [ 1.4,  0.3, -0.2]]]]])
        grid = torch.tensor([[[[[ 0.2, 0.2,  0.3],[-0.4, 0.2, -0.3],[-0.9, 0.2,  0.3],[-0.9, 0.9, -0.6]],
                            [[ 0.2, 0.2,  0.3],[-0.4, 0.2, -0.3],[-0.9, 0.2,  0.3],[-0.9, 0.9, -0.6]]]]])
        result = F.grid_sample(x, grid, mode='bilinear', align_corners=True)
        """
    )
    obj.run(pytorch_code, ["result"], check_value=False, check_stop_gradient=False)


def test_case_6():
    pytorch_code = textwrap.dedent(
        """
        import torch
        import torch.nn.functional as F
        x = torch.tensor([[[[[-0.6,  0.8, -0.5], [-0.5,  0.2,  1.2], [ 1.4,  0.3, -0.2]]]]])
        grid = torch.tensor([[[[[ 0.2, 0.2,  0.3],[-0.4, 0.2, -0.3],[-0.9, 0.2,  0.3],[-0.9, 0.9, -0.6]],
                            [[ 0.2, 0.2,  0.3],[-0.4, 0.2, -0.3],[-0.9, 0.2,  0.3],[-0.9, 0.9, -0.6]]]]])
        result = F.grid_sample(input=x, grid=grid, mode='bilinear', padding_mode="border", align_corners=True)
        """
    )
    obj.run(pytorch_code, ["result"], check_value=False, check_stop_gradient=False)


def test_case_7():
    pytorch_code = textwrap.dedent(
        """
        import torch
        import torch.nn.functional as F
        x = torch.tensor([[[[[-0.6,  0.8, -0.5], [-0.5,  0.2,  1.2], [ 1.4,  0.3, -0.2]]]]])
        grid = torch.tensor([[[[[ 0.2, 0.2,  0.3],[-0.4, 0.2, -0.3],[-0.9, 0.2,  0.3],[-0.9, 0.9, -0.6]],
                            [[ 0.2, 0.2,  0.3],[-0.4, 0.2, -0.3],[-0.9, 0.2,  0.3],[-0.9, 0.9, -0.6]]]]])
        result = F.grid_sample(input=x, padding_mode="border", align_corners=True, grid=grid, mode='bilinear')
        """
    )
    obj.run(pytorch_code, ["result"], check_value=False, check_stop_gradient=False)


def test_case_8():
    pytorch_code = textwrap.dedent(
        """
        import torch
        import torch.nn.functional as F
        x = torch.tensor([[[[[-0.6,  0.8, -0.5], [-0.5,  0.2,  1.2], [ 1.4,  0.3, -0.2]]]]])
        grid = torch.tensor([[[[[ 0.2, 0.2,  0.3],[-0.4, 0.2, -0.3],[-0.9, 0.2,  0.3],[-0.9, 0.9, -0.6]],
                            [[ 0.2, 0.2,  0.3],[-0.4, 0.2, -0.3],[-0.9, 0.2,  0.3],[-0.9, 0.9, -0.6]]]]])
        result = F.grid_sample(x, grid, 'bilinear', "border", True)
        """
    )
    obj.run(pytorch_code, ["result"], check_value=False, check_stop_gradient=False)
