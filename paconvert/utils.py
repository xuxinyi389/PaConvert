# Copyright (c) 2022  PaddlePaddle Authors. All Rights Reserved.
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

import collections
import os
import textwrap


class UniqueNameGenerator:
    def __init__(self):
        self.ids = collections.defaultdict(int)

    def __call__(self, key):
        counter = self.ids[key]
        self.ids[key] += 1
        return "_".join([key, str(counter)])


Generator = UniqueNameGenerator()


def get_unique_name(key):
    return Generator(key)


class AuxFileHelper(object):
    _instance = None

    def __init__(self, fileName=None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if fileName:
            self.fileName = fileName
            self.ids = collections.defaultdict(int)

    def write_code(self, code, torch_api):
        if len(self.ids) == 0:
            CODE_CONTENT = textwrap.dedent(
                """
                # This file is generated by PaConvert ToolKit, please Don't edit it!
                import paddle
                """
            )
            if not os.path.exists(os.path.dirname(self.fileName)):
                os.makedirs(os.path.dirname(self.fileName))

            with open(self.fileName, "w") as file:
                file.write(CODE_CONTENT)

        if self.ids[code] == 0:
            with open(self.fileName, "a") as file:
                file.write(code)

        self.ids[code] += 1

    def __new__(cls, fileName=None, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance


def log_debug(logger, msg, file=None, line=None):
    if file:
        if line:
            msg = "[{}:{}] {}".format(file, line, msg)
        else:
            msg = "[{}] {}".format(file, msg)
    else:
        msg = "{}".format(msg)
    logger.debug(msg)


def log_info(logger, msg, file=None, line=None):
    if file:
        if line:
            msg = "[{}:{}] {}".format(file, line, msg)
        else:
            msg = "[{}] {}".format(file, msg)
    else:
        msg = "{}".format(msg)
    logger.info(msg)


def process_reduce_and_size_average(kwargs):
    if "size_average" in kwargs:
        size_average = kwargs.pop("size_average")
        if "True" in size_average:
            size_average = True
        elif "False" in size_average:
            size_average = False
        else:
            size_average = None
    else:
        size_average = None

    if "reduce" in kwargs:
        reduce = kwargs.pop("reduce")
        if "True" in reduce:
            reduce = True
        elif "False" in reduce:
            reduce = False
        else:
            reduce = None
    else:
        reduce = None

    if size_average is not None or reduce is not None:
        if size_average is None:
            size_average = True
        if reduce is None:
            reduce = True

        if size_average and reduce:
            reduction = '"""mean"""'
        elif reduce:
            reduction = '"""sum"""'
        else:
            reduction = '"""none"""'

        kwargs["reduction"] = reduction
