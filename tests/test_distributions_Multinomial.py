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

obj = APIBase("torch.distributions.Multinomial")


def test_case_1():
    pytorch_code = textwrap.dedent(
        """
        import torch
        m = torch.distributions.Multinomial(1, torch.tensor([0.3]))
        result = m.sample([100])
        """
    )
    obj.run(pytorch_code, ["result"], check_value=False)


def test_case_2():
    pytorch_code = textwrap.dedent(
        """
        import torch
        m = torch.distributions.Multinomial(total_count=1, probs=torch.tensor([0.3]), logits=None)
        result = m.sample([100])
        """
    )
    obj.run(
        pytorch_code,
        ["result"],
        check_value=False,
        unsupport=True,
        reason="paddle does not support logits temporarily",
    )


def test_case_3():
    pytorch_code = textwrap.dedent(
        """
        import torch
        m = torch.distributions.Multinomial(1, torch.tensor([0.3]), validate_args=False)
        result = m.sample([100])
        """
    )
    obj.run(pytorch_code, ["result"], check_value=False)


def test_case_4():
    pytorch_code = textwrap.dedent(
        """
        import torch
        m = torch.distributions.multinomial.Multinomial(1, torch.tensor([0.3]), validate_args=False)
        result = m.sample([100])
        """
    )
    obj.run(pytorch_code, ["result"], check_value=False)


def test_case_5():
    pytorch_code = textwrap.dedent(
        """
        import torch
        m = torch.distributions.multinomial.Multinomial(total_count=1, probs=torch.tensor([0.3]), validate_args=False)
        result = m.sample([100])
        """
    )
    obj.run(pytorch_code, ["result"], check_value=False)


def test_case_6():
    pytorch_code = textwrap.dedent(
        """
        import torch
        m = torch.distributions.multinomial.Multinomial(total_count=1, validate_args=False, probs=torch.tensor([0.3]))
        result = m.sample([100])
        """
    )
    obj.run(pytorch_code, ["result"], check_value=False)


def test_case_7():
    pytorch_code = textwrap.dedent(
        """
        import torch
        m = torch.distributions.Multinomial(total_count=1, probs=torch.tensor([0.3]), logits=None, validate_args=False)
        result = m.sample([100])
        """
    )
    obj.run(
        pytorch_code,
        ["result"],
        check_value=False,
        unsupport=True,
        reason="paddle does not support logits temporarily",
    )


def test_case_8():
    pytorch_code = textwrap.dedent(
        """
        import torch
        m = torch.distributions.Multinomial(total_count=1, logits=None, probs=torch.tensor([0.3]), validate_args=False)
        result = m.sample([100])
        """
    )
    obj.run(
        pytorch_code,
        ["result"],
        check_value=False,
        unsupport=True,
        reason="paddle does not support logits temporarily",
    )


def test_case_9():
    pytorch_code = textwrap.dedent(
        """
        import torch
        m = torch.distributions.Multinomial(1, torch.tensor([0.3]), None, False)
        result = m.sample([100])
        """
    )
    obj.run(
        pytorch_code,
        ["result"],
        check_value=False,
        unsupport=True,
        reason="paddle does not support logits temporarily",
    )


def test_case_10():
    pytorch_code = textwrap.dedent(
        """
        import torch
        m = torch.distributions.Multinomial(None, torch.tensor([0.3]), 0.8, False)
        result = m.sample([100])
        """
    )
    obj.run(
        pytorch_code,
        ["result"],
        check_value=False,
        unsupport=True,
        reason="paddle does not support logits temporarily",
    )
