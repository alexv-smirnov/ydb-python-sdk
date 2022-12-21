# -*- coding: utf-8 -*-
# flake8: noqa
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: ydb_table_v1.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from ydb._grpc.v4.protos import ydb_table_pb2 as protos_dot_ydb__table__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x12ydb_table_v1.proto\x12\x0cYdb.Table.V1\x1a\x16protos/ydb_table.proto2\xa4\x0e\n\x0cTableService\x12R\n\rCreateSession\x12\x1f.Ydb.Table.CreateSessionRequest\x1a .Ydb.Table.CreateSessionResponse\x12R\n\rDeleteSession\x12\x1f.Ydb.Table.DeleteSessionRequest\x1a .Ydb.Table.DeleteSessionResponse\x12\x46\n\tKeepAlive\x12\x1b.Ydb.Table.KeepAliveRequest\x1a\x1c.Ydb.Table.KeepAliveResponse\x12L\n\x0b\x43reateTable\x12\x1d.Ydb.Table.CreateTableRequest\x1a\x1e.Ydb.Table.CreateTableResponse\x12\x46\n\tDropTable\x12\x1b.Ydb.Table.DropTableRequest\x1a\x1c.Ydb.Table.DropTableResponse\x12I\n\nAlterTable\x12\x1c.Ydb.Table.AlterTableRequest\x1a\x1d.Ydb.Table.AlterTableResponse\x12\x46\n\tCopyTable\x12\x1b.Ydb.Table.CopyTableRequest\x1a\x1c.Ydb.Table.CopyTableResponse\x12I\n\nCopyTables\x12\x1c.Ydb.Table.CopyTablesRequest\x1a\x1d.Ydb.Table.CopyTablesResponse\x12O\n\x0cRenameTables\x12\x1e.Ydb.Table.RenameTablesRequest\x1a\x1f.Ydb.Table.RenameTablesResponse\x12R\n\rDescribeTable\x12\x1f.Ydb.Table.DescribeTableRequest\x1a .Ydb.Table.DescribeTableResponse\x12[\n\x10\x45xplainDataQuery\x12\".Ydb.Table.ExplainDataQueryRequest\x1a#.Ydb.Table.ExplainDataQueryResponse\x12[\n\x10PrepareDataQuery\x12\".Ydb.Table.PrepareDataQueryRequest\x1a#.Ydb.Table.PrepareDataQueryResponse\x12[\n\x10\x45xecuteDataQuery\x12\".Ydb.Table.ExecuteDataQueryRequest\x1a#.Ydb.Table.ExecuteDataQueryResponse\x12\x61\n\x12\x45xecuteSchemeQuery\x12$.Ydb.Table.ExecuteSchemeQueryRequest\x1a%.Ydb.Table.ExecuteSchemeQueryResponse\x12[\n\x10\x42\x65ginTransaction\x12\".Ydb.Table.BeginTransactionRequest\x1a#.Ydb.Table.BeginTransactionResponse\x12^\n\x11\x43ommitTransaction\x12#.Ydb.Table.CommitTransactionRequest\x1a$.Ydb.Table.CommitTransactionResponse\x12\x64\n\x13RollbackTransaction\x12%.Ydb.Table.RollbackTransactionRequest\x1a&.Ydb.Table.RollbackTransactionResponse\x12g\n\x14\x44\x65scribeTableOptions\x12&.Ydb.Table.DescribeTableOptionsRequest\x1a\'.Ydb.Table.DescribeTableOptionsResponse\x12N\n\x0fStreamReadTable\x12\x1b.Ydb.Table.ReadTableRequest\x1a\x1c.Ydb.Table.ReadTableResponse0\x01\x12I\n\nBulkUpsert\x12\x1c.Ydb.Table.BulkUpsertRequest\x1a\x1d.Ydb.Table.BulkUpsertResponse\x12j\n\x16StreamExecuteScanQuery\x12\".Ydb.Table.ExecuteScanQueryRequest\x1a*.Ydb.Table.ExecuteScanQueryPartialResponse0\x01\x42I\n\x11tech.ydb.table.v1Z4github.com/ydb-platform/ydb-go-genproto/Ydb_Table_V1b\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'ydb_table_v1_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\021tech.ydb.table.v1Z4github.com/ydb-platform/ydb-go-genproto/Ydb_Table_V1'
  _TABLESERVICE._serialized_start=61
  _TABLESERVICE._serialized_end=1889
# @@protoc_insertion_point(module_scope)