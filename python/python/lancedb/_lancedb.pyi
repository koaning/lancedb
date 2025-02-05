from typing import Dict, List, Optional

import pyarrow as pa

class Index:
    @staticmethod
    def ivf_pq(
        distance_type: Optional[str],
        num_partitions: Optional[int],
        num_sub_vectors: Optional[int],
        max_iterations: Optional[int],
        sample_rate: Optional[int],
    ) -> Index: ...
    @staticmethod
    def btree() -> Index: ...

class Connection(object):
    async def table_names(
        self, start_after: Optional[str], limit: Optional[int]
    ) -> list[str]: ...
    async def create_table(
        self, name: str, mode: str, data: pa.RecordBatchReader
    ) -> Table: ...
    async def create_empty_table(
        self, name: str, mode: str, schema: pa.Schema
    ) -> Table: ...

class Table:
    def name(self) -> str: ...
    def __repr__(self) -> str: ...
    async def schema(self) -> pa.Schema: ...
    async def add(self, data: pa.RecordBatchReader, mode: str) -> None: ...
    async def update(self, updates: Dict[str, str], where: Optional[str]) -> None: ...
    async def count_rows(self, filter: Optional[str]) -> int: ...
    async def create_index(
        self, column: str, config: Optional[Index], replace: Optional[bool]
    ): ...
    async def version(self) -> int: ...
    async def checkout(self, version): ...
    async def checkout_latest(self): ...
    async def restore(self): ...
    async def list_indices(self) -> List[IndexConfig]: ...

class IndexConfig:
    index_type: str
    columns: List[str]

async def connect(
    uri: str,
    api_key: Optional[str],
    region: Optional[str],
    host_override: Optional[str],
    read_consistency_interval: Optional[float],
) -> Connection: ...
