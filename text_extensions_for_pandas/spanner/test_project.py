#
#  Copyright (c) 2020 IBM Corp.
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#  http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.
#

from text_extensions_for_pandas.io.spacy import make_tokens_and_features
from text_extensions_for_pandas.spanner.project import *
from text_extensions_for_pandas.util import TestBase

import spacy
_SPACY_LANGUAGE_MODEL = spacy.load("en_core_web_sm")


class ProjectTest(TestBase):
    def test_lemmatize(self):
        test_text = "If Barbie is so popular, why do you have to buy Barbie's friends?"
        df = make_tokens_and_features(test_text, _SPACY_LANGUAGE_MODEL)
        self.assertIn("lemma", df.columns)
        norm = lemmatize(df["span"], df)
        expected = ['if', 'Barbie', 'be', 'so', 'popular', ',', 'why', 'do', 'you', 'have',
                    'to', 'buy', 'Barbie', "'s", 'friend', '?']
        self.assertListEqual(norm, expected)
