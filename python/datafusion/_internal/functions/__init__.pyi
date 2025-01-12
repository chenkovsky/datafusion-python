# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.

from typing import Any, List, Optional, Protocol
from ..expr import Expr, SortExpr, CaseBuilder, WindowFrame
from .. import SessionContext
from ...common import NullTreatment

def in_list(expr: Expr, value: List[Expr], negated: bool) -> Expr: ...

def make_array(exprs: List[Expr]) -> Expr: ...

def array_concat(exprs: List[Expr]) -> Expr: ...

def array_cat(exprs: List[Expr]) -> Expr: ...

def array_position(array: Expr, element: Expr, index: Optional[int] = None) -> Expr: ...

def array_slice(array: Expr, begin: Expr, end: Expr, stride: Optional[Expr] = None) -> Expr: ...

def digest(value: Expr, method: Expr) -> Expr: ...

def concat(args: List[Expr]) -> Expr: ...

def concat_ws(sep: str, args: List[Expr]) -> Expr: ...

def regexp_like(values: Expr, regex: Expr, flags: Optional[Expr] = None) -> Expr: ...

def regexp_match(values: Expr, regex: Expr, flags: Optional[Expr] = None) -> Expr: ...

def regexp_replace(string: Expr, pattern: Expr, replacement: Expr, flags: Optional[Expr] = None) -> Expr: ...

def order_by(expr: Expr, asc: bool, nulls_first: bool) -> SortExpr: ...

def alias(expr: Expr, name: str) -> Expr: ...

def col(name: str) -> Expr: ...

def case(expr: Expr) -> CaseBuilder: ...

def when(when: Expr, then: Expr) -> CaseBuilder: ...

def window(name: str, args: List[Expr], partition_by: Optional[List[Expr]], order_by: Optional[List[SortExpr]], window_frame: Optional[WindowFrame], ctx: Optional[SessionContext]) -> Expr: ...

def abs(num: Expr) -> Expr: ...

def acos(num: Expr) -> Expr: ...

def acosh(num: Expr) -> Expr: ...

def ascii(num: Expr) -> Expr: ...

def asin(num: Expr) -> Expr: ...

def asinh(num: Expr) -> Expr: ...

def atan(num: Expr) -> Expr: ...

def atanh(num: Expr) -> Expr: ...

def atan2(y: Expr, x: Expr) -> Expr: ...

def bit_length(arg: Expr) -> Expr: ...

def btrim(*args: Expr) -> Expr: ...

def cbrt(num: Expr) -> Expr: ...

def ceil(num: Expr) -> Expr: ...

def character_length(string: Expr) -> Expr: ...

def length(string: Expr) -> Expr: ...

def char_length(string: Expr) -> Expr: ...

def chr(arg: Expr) -> Expr: ...

def coalesce(*args: Expr) -> Expr: ...

def cos(num: Expr) -> Expr: ...

def cosh(num: Expr) -> Expr: ...

def cot(num: Expr) -> Expr: ...

def degrees(num: Expr) -> Expr: ...

def decode(input: Expr, encoding: Expr) -> Expr: ...

def encode(input: Expr, encoding: Expr) -> Expr: ...

def ends_with(string: Expr, suffix: Expr) -> Expr: ...

def exp(num: Expr) -> Expr: ...

def factorial(num: Expr) -> Expr: ...

def floor(num: Expr) -> Expr: ...

def gcd(x: Expr, y: Expr) -> Expr: ...

def initcap(string: Expr) -> Expr: ...

def isnan(num: Expr) -> Expr: ...

def iszero(num: Expr) -> Expr: ...

def levenshtein(string1: Expr, string2: Expr) -> Expr: ...

def lcm(x: Expr, y: Expr) -> Expr: ...

def left(string: Expr, n: Expr) -> Expr: ...

def ln(num: Expr) -> Expr: ...

def log(base: Expr, num: Expr) -> Expr: ...

def log10(num: Expr) -> Expr: ...

def log2(num: Expr) -> Expr: ...

def lower(arg1: Expr) -> Expr: ...

def lpad(*args: Expr) -> Expr: ...

def ltrim(*args: Expr) -> Expr: ...

def md5(input_arg: Expr) -> Expr: ...

def nanvl(x: Expr, y: Expr) -> Expr: ...

def nvl(x: Expr, y: Expr) -> Expr: ...

def nullif(arg_1: Expr, arg_2: Expr) -> Expr: ...

def octet_length(args: Expr) -> Expr: ...

def overlay(*args: Expr) -> Expr: ...

def pi() -> Expr: ...

def power(base: Expr, exponent: Expr) -> Expr: ...

def radians(num: Expr) -> Expr: ...

def repeat(string: Expr, n: Expr) -> Expr: ...

def replace(string: Expr, from_: Expr, to: Expr) -> Expr: ...

def reverse(string: Expr) -> Expr: ...

def right(string: Expr, n: Expr) -> Expr: ...

def round(*args: Expr) -> Expr: ...

def rpad(*args: Expr) -> Expr: ...

def rtrim(*args: Expr) -> Expr: ...

def sha224(input_arg1: Expr) -> Expr: ...

def sha256(input_arg1: Expr) -> Expr: ...

def sha384(input_arg1: Expr) -> Expr: ...

def sha512(input_arg1: Expr) -> Expr: ...

def signum(num: Expr) -> Expr: ...

def sin(num: Expr) -> Expr: ...

def sinh(num: Expr) -> Expr: ...

def split_part(string: Expr, delimiter: Expr, index: Expr) -> Expr: ...

def sqrt(num: Expr) -> Expr: ...

def starts_with(string: Expr, prefix: Expr) -> Expr: ...

def strpos(string: Expr, substring: Expr) -> Expr: ...

def substr(string: Expr, position: Expr) -> Expr: ...

def substr_index(string: Expr, delimiter: Expr, count: Expr) -> Expr: ...

def substring(string: Expr, position: Expr, length: Expr) -> Expr: ...

def find_in_set(string: Expr, string_list: Expr) -> Expr: ...

def tan(num: Expr) -> Expr: ...

def tanh(num: Expr) -> Expr: ...

def to_hex(arg1: Expr) -> Expr: ...

def now() -> Expr: ...

def to_timestamp(*args: Expr) -> Expr: ...

def to_timestamp_millis(*args: Expr) -> Expr: ...

def to_timestamp_micros(*args: Expr) -> Expr: ...

def to_timestamp_seconds(*args: Expr) -> Expr: ...

def to_unixtime(*args: Expr) -> Expr: ...

def current_date() -> Expr: ...

def current_time() -> Expr: ...

def date_part(part: Expr, date: Expr) -> Expr: ...

def date_trunc(part: Expr, date: Expr) -> Expr: ...

def date_bin(stride: Expr, source: Expr, origin: Expr) -> Expr: ...

def make_date(year: Expr, month: Expr, day: Expr) -> Expr: ...

def translate(string: Expr, from_: Expr, to: Expr) -> Expr: ...

def trim(*args: Expr) -> Expr: ...

def trunc(*args: Expr) -> Expr: ...

def upper(arg1: Expr) -> Expr: ...

def uuid() -> Expr: ...

def struct(*args: Expr) -> Expr: ...

def named_struct(*args: Expr) -> Expr: ...

def from_unixtime(unixtime: Expr) -> Expr: ...

def arrow_typeof(arg_1: Expr) -> Expr: ...

def arrow_cast(arg_1: Expr, datatype: Expr) -> Expr: ...

def random() -> Expr: ...

def array_append(array: Expr, element: Expr) -> Expr: ...

def array_to_string(array: Expr, delimiter: Expr) -> Expr: ...

def array_dims(array: Expr) -> Expr: ...

def array_distinct(array: Expr) -> Expr: ...

def array_element(array: Expr, element: Expr) -> Expr: ...

def array_empty(array: Expr) -> Expr: ...

def array_length(array: Expr) -> Expr: ...

def array_has(first_array: Expr, second_array: Expr) -> Expr: ...

def array_has_all(first_array: Expr, second_array: Expr) -> Expr: ...

def array_has_any(first_array: Expr, second_array: Expr) -> Expr: ...

def array_positions(array: Expr, element: Expr) -> Expr: ...

def array_ndims(array: Expr) -> Expr: ...

def array_prepend(element: Expr, array: Expr) -> Expr: ...

def array_pop_back(array: Expr) -> Expr: ...

def array_pop_front(array: Expr) -> Expr: ...

def array_remove(array: Expr, element: Expr) -> Expr: ...

def array_remove_n(array: Expr, element: Expr, max: Expr) -> Expr: ...

def array_remove_all(array: Expr, element: Expr) -> Expr: ...

def array_repeat(element: Expr, count: Expr) -> Expr: ...

def array_replace(array: Expr, from_: Expr, to: Expr) -> Expr: ...

def array_replace_n(array: Expr, from_: Expr, to: Expr, mx: Expr) -> Expr: ...

def array_replace_all(array: Expr, from_: Expr, to: Expr) -> Expr: ...

def array_sort(array: Expr, desc: Expr, null_first: Expr) -> Expr: ...

def array_intersect(first_array: Expr, second_array: Expr) -> Expr: ...

def array_union(array1: Expr, array2: Expr) -> Expr: ...

def array_except(first_array: Expr, second_array: Expr) -> Expr: ...

def array_resize(array: Expr, size: Expr, value: Expr) -> Expr: ...

def cardinality(array: Expr) -> Expr: ...

def flatten(array: Expr) -> Expr: ...

def range(start: Expr, stop: Expr, step: Expr) -> Expr: ...

class AggregateFunction(Protocol):
    def __call__(self, exp: Expr, *, distinct: Optional[bool] = None, filter: Optional[Expr] = None, order_by: Optional[List[SortExpr]] = None, null_treatment: Optional[int] = None) -> Expr:
        ...

class AggregateFunctionYX(Protocol):
    def __call__(self, y: Expr, x: Expr, *, distinct: Optional[bool] = None, filter: Optional[Expr] = None, order_by: Optional[List[SortExpr]] = None, null_treatment: Optional[int] = None) -> Expr:
        ...

array_agg: AggregateFunction
max: AggregateFunction
min: AggregateFunction
avg: AggregateFunction
sum: AggregateFunction
bit_and: AggregateFunction
bit_or: AggregateFunction
bit_xor: AggregateFunction
bool_and: AggregateFunction
bool_or: AggregateFunction
corr: AggregateFunctionYX
count: AggregateFunction
covar_samp: AggregateFunctionYX
covar_pop: AggregateFunctionYX
median: AggregateFunction
regr_slope: AggregateFunctionYX
regr_intercept: AggregateFunctionYX
regr_count: AggregateFunctionYX
regr_r2: AggregateFunctionYX
regr_avgx: AggregateFunctionYX
regr_avgy: AggregateFunctionYX
regr_sxx: AggregateFunctionYX
regr_syy: AggregateFunctionYX
regr_sxy: AggregateFunctionYX
stddev: AggregateFunction
stddev_pop: AggregateFunction
var_sample: AggregateFunction
var_pop: AggregateFunction
approx_distinct: AggregateFunction
approx_median: AggregateFunction

def approx_percentile_cont(expression: Expr, percentile: float, num_centroids: Optional[int] = None, filter: Optional[Expr] = None) -> Expr: ...

def approx_percentile_cont_with_weight(
    expression: Expr,
    weight: Expr,
    percentile: float,
    filter: Optional[Expr] = None,
) -> Expr: ...

last_value: AggregateFunction

def first_value(expr: Expr, distinct: Optional[bool] = None, filter: Optional[Expr] = None, order_by: Optional[List[SortExpr]] = None, null_treatment: Optional[int] = None) -> Expr: ...

def nth_value(expr: Expr, n: int, distinct: Optional[bool] = None, filter: Optional[Expr] = None, order_by: Optional[List[SortExpr]] = None, null_treatment: Optional[int] = None) -> Expr:
    ...

def string_agg(expr: Expr, delimiter: str, distinct: Optional[bool] = None, filter: Optional[Expr] = None, order_by: Optional[List[SortExpr]] = None, null_treatment: Optional[int] = None) -> Expr:
    ...

def lead(arg: Expr, shift_offset: int, default_value: Optional[Any] = None, partition_by: Optional[List[Expr]] = None, order_by: Optional[List[SortExpr]] = None) -> Expr:
    ...

def lag(arg: Expr, shift_offset: int, default_value: Optional[Any] = None, partition_by: Optional[List[Expr]] = None, order_by: Optional[List[SortExpr]] = None) -> Expr:
    ...

class WindowFunction(Protocol):
    def __call__(self, partition_by: Optional[List[Expr]] = None, order_by: Optional[List[SortExpr]] = None) -> Expr:
        ...

row_number: WindowFunction
rank: WindowFunction
dense_rank: WindowFunction
percent_rank: WindowFunction
cume_dist: WindowFunction

def ntile(arg: Expr, partition_by: Optional[List[Expr]] = None, order_by: Optional[List[SortExpr]] = None)  -> Expr:
    ...

