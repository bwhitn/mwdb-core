"""Initial version

Revision ID: 2e692ea445a1
Revises: 
Create Date: 2020-05-25 20:05:26.994945

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '2e692ea445a1'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('group',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(length=32), nullable=False),
    sa.Column('capabilities', postgresql.ARRAY(sa.Text()), server_default='{}', nullable=False),
    sa.Column('private', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_group_name'), 'group', ['name'], unique=True)
    op.create_table('metakey_definition',
    sa.Column('key', sa.String(length=64), nullable=False),
    sa.Column('label', sa.String(length=64), nullable=True),
    sa.Column('description', sa.Text(), nullable=True),
    sa.Column('url_template', sa.Text(), nullable=True),
    sa.Column('hidden', sa.Boolean(), nullable=False),
    sa.PrimaryKeyConstraint('key')
    )
    op.create_table('object',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('type', sa.String(length=50), nullable=True),
    sa.Column('dhash', sa.String(length=64), nullable=True),
    sa.Column('upload_time', sa.DateTime(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_object_dhash'), 'object', ['dhash'], unique=True)
    op.create_index(op.f('ix_object_upload_time'), 'object', ['upload_time'], unique=False)
    op.create_table('tag',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('tag', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_tag_tag'), 'tag', ['tag'], unique=True)
    op.create_table('user',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('login', sa.String(length=32), nullable=False),
    sa.Column('email', sa.String(length=128), nullable=True),
    sa.Column('password_hash', sa.String(length=128), nullable=True),
    sa.Column('version_uid', sa.String(length=16), nullable=True),
    sa.Column('password_ver', sa.String(length=16), nullable=True),
    sa.Column('identity_ver', sa.String(length=16), nullable=True),
    sa.Column('additional_info', sa.String(), nullable=True),
    sa.Column('disabled', sa.Boolean(), nullable=False),
    sa.Column('pending', sa.Boolean(), nullable=False),
    sa.Column('requested_on', sa.DateTime(), nullable=True),
    sa.Column('registered_on', sa.DateTime(), nullable=True),
    sa.Column('registered_by', sa.Integer(), nullable=True),
    sa.Column('logged_on', sa.DateTime(), nullable=True),
    sa.Column('set_password_on', sa.DateTime(), nullable=True),
    sa.Column('feed_quality', sa.String(length=32), server_default='high', nullable=True),
    sa.ForeignKeyConstraint(['registered_by'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_user_login'), 'user', ['login'], unique=True)
    op.create_table('api_key',
    sa.Column('id', postgresql.UUID(as_uuid=True), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('issued_on', sa.DateTime(), nullable=True),
    sa.Column('issued_by', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['issued_by'], ['user.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('comment',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('comment', sa.String(), nullable=False),
    sa.Column('timestamp', sa.DateTime(), nullable=False),
    sa.Column('object_id', sa.Integer(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['object_id'], ['object.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('file',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('file_name', sa.String(), nullable=True),
    sa.Column('file_size', sa.Integer(), nullable=False),
    sa.Column('file_type', sa.Text(), nullable=True),
    sa.Column('md5', sa.String(length=32), nullable=False),
    sa.Column('crc32', sa.String(length=8), nullable=False),
    sa.Column('sha1', sa.String(length=40), nullable=False),
    sa.Column('sha256', sa.String(length=64), nullable=False),
    sa.Column('sha512', sa.String(length=128), nullable=False),
    sa.Column('humanhash', sa.String(), nullable=False),
    sa.Column('ssdeep', sa.String(length=255), nullable=True),
    sa.ForeignKeyConstraint(['id'], ['object.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_file_crc32'), 'file', ['crc32'], unique=False)
    op.create_index(op.f('ix_file_file_name'), 'file', ['file_name'], unique=False)
    op.create_index(op.f('ix_file_file_size'), 'file', ['file_size'], unique=False)
    op.create_index(op.f('ix_file_file_type'), 'file', ['file_type'], unique=False)
    op.create_index(op.f('ix_file_humanhash'), 'file', ['humanhash'], unique=False)
    op.create_index(op.f('ix_file_md5'), 'file', ['md5'], unique=False)
    op.create_index(op.f('ix_file_sha1'), 'file', ['sha1'], unique=False)
    op.create_index(op.f('ix_file_sha256'), 'file', ['sha256'], unique=True)
    op.create_index(op.f('ix_file_sha512'), 'file', ['sha512'], unique=False)
    op.create_index(op.f('ix_file_ssdeep'), 'file', ['ssdeep'], unique=False)
    op.create_table('member',
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('group_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['group_id'], ['group.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], )
    )
    op.create_table('metakey',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('object_id', sa.Integer(), nullable=True),
    sa.Column('key', sa.String(length=64), nullable=True),
    sa.Column('value', sa.Text(), nullable=True),
    sa.ForeignKeyConstraint(['key'], ['metakey_definition.key'], ),
    sa.ForeignKeyConstraint(['object_id'], ['object.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('object_id', 'key', 'value')
    )
    op.create_index(op.f('ix_metakey_key'), 'metakey', ['key'], unique=False)
    op.create_index(op.f('ix_metakey_value'), 'metakey', ['value'], unique=False)
    op.create_table('metakey_permission',
    sa.Column('key', sa.String(length=64), nullable=False),
    sa.Column('group_id', sa.Integer(), autoincrement=False, nullable=False),
    sa.Column('can_read', sa.Boolean(), nullable=False),
    sa.Column('can_set', sa.Boolean(), nullable=False),
    sa.ForeignKeyConstraint(['group_id'], ['group.id'], ),
    sa.ForeignKeyConstraint(['key'], ['metakey_definition.key'], ),
    sa.PrimaryKeyConstraint('key', 'group_id')
    )
    op.create_index(op.f('ix_metakey_permission_group_id'), 'metakey_permission', ['group_id'], unique=False)
    op.create_index(op.f('ix_metakey_permission_key'), 'metakey_permission', ['key'], unique=False)
    op.create_index('ix_metakey_permission_metakey_group', 'metakey_permission', ['key', 'group_id'], unique=True)
    op.create_table('object_tag',
    sa.Column('object_id', sa.Integer(), nullable=True),
    sa.Column('tag_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['object_id'], ['object.id'], ),
    sa.ForeignKeyConstraint(['tag_id'], ['tag.id'], )
    )
    op.create_index('ix_object_tag_object_child', 'object_tag', ['object_id', 'tag_id'], unique=True)
    op.create_index(op.f('ix_object_tag_object_id'), 'object_tag', ['object_id'], unique=False)
    op.create_index(op.f('ix_object_tag_tag_id'), 'object_tag', ['tag_id'], unique=False)
    op.create_table('permission',
    sa.Column('object_id', sa.Integer(), autoincrement=False, nullable=False),
    sa.Column('group_id', sa.Integer(), autoincrement=False, nullable=False),
    sa.Column('access_time', sa.DateTime(), nullable=False),
    sa.Column('reason_type', sa.String(length=32), nullable=True),
    sa.Column('related_object_id', sa.Integer(), nullable=True),
    sa.Column('related_user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['group_id'], ['group.id'], ),
    sa.ForeignKeyConstraint(['object_id'], ['object.id'], ),
    sa.ForeignKeyConstraint(['related_object_id'], ['object.id'], ),
    sa.ForeignKeyConstraint(['related_user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('object_id', 'group_id')
    )
    op.create_index(op.f('ix_permission_access_time'), 'permission', ['access_time'], unique=False)
    op.create_index(op.f('ix_permission_group_id'), 'permission', ['group_id'], unique=False)
    op.create_index('ix_permission_group_object', 'permission', ['object_id', 'group_id'], unique=True)
    op.create_index(op.f('ix_permission_object_id'), 'permission', ['object_id'], unique=False)
    op.create_index(op.f('ix_permission_related_user_id'), 'permission', ['related_user_id'], unique=False)
    op.create_table('relation',
    sa.Column('parent_id', sa.Integer(), nullable=True),
    sa.Column('child_id', sa.Integer(), nullable=True),
    sa.Column('creation_time', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['child_id'], ['object.id'], ),
    sa.ForeignKeyConstraint(['parent_id'], ['object.id'], )
    )
    op.create_index(op.f('ix_relation_child_id'), 'relation', ['child_id'], unique=False)
    op.create_index('ix_relation_parent_child', 'relation', ['parent_id', 'child_id'], unique=True)
    op.create_index(op.f('ix_relation_parent_id'), 'relation', ['parent_id'], unique=False)
    op.create_table('static_config',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('family', sa.String(length=32), nullable=True),
    sa.Column('config_type', sa.String(length=32), server_default='static', nullable=False),
    sa.Column('cfg', postgresql.JSON(astext_type=sa.Text()), nullable=False),
    sa.ForeignKeyConstraint(['id'], ['object.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_static_config_config_type'), 'static_config', ['config_type'], unique=False)
    op.create_index(op.f('ix_static_config_family'), 'static_config', ['family'], unique=False)
    op.create_table('text_blob',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('blob_name', sa.String(), nullable=True),
    sa.Column('blob_size', sa.Integer(), nullable=False),
    sa.Column('blob_type', sa.String(length=32), nullable=True),
    sa.Column('content', sa.String(), nullable=False),
    sa.Column('last_seen', sa.DateTime(), nullable=False),
    sa.ForeignKeyConstraint(['id'], ['object.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_text_blob_blob_name'), 'text_blob', ['blob_name'], unique=False)
    op.create_index(op.f('ix_text_blob_blob_size'), 'text_blob', ['blob_size'], unique=False)
    op.create_index(op.f('ix_text_blob_blob_type'), 'text_blob', ['blob_type'], unique=False)
    op.create_index(op.f('ix_text_blob_last_seen'), 'text_blob', ['last_seen'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_text_blob_last_seen'), table_name='text_blob')
    op.drop_index(op.f('ix_text_blob_blob_type'), table_name='text_blob')
    op.drop_index(op.f('ix_text_blob_blob_size'), table_name='text_blob')
    op.drop_index(op.f('ix_text_blob_blob_name'), table_name='text_blob')
    op.drop_table('text_blob')
    op.drop_index(op.f('ix_static_config_family'), table_name='static_config')
    op.drop_index(op.f('ix_static_config_config_type'), table_name='static_config')
    op.drop_table('static_config')
    op.drop_index(op.f('ix_relation_parent_id'), table_name='relation')
    op.drop_index('ix_relation_parent_child', table_name='relation')
    op.drop_index(op.f('ix_relation_child_id'), table_name='relation')
    op.drop_table('relation')
    op.drop_index(op.f('ix_permission_related_user_id'), table_name='permission')
    op.drop_index(op.f('ix_permission_object_id'), table_name='permission')
    op.drop_index('ix_permission_group_object', table_name='permission')
    op.drop_index(op.f('ix_permission_group_id'), table_name='permission')
    op.drop_index(op.f('ix_permission_access_time'), table_name='permission')
    op.drop_table('permission')
    op.drop_index(op.f('ix_object_tag_tag_id'), table_name='object_tag')
    op.drop_index(op.f('ix_object_tag_object_id'), table_name='object_tag')
    op.drop_index('ix_object_tag_object_child', table_name='object_tag')
    op.drop_table('object_tag')
    op.drop_index('ix_metakey_permission_metakey_group', table_name='metakey_permission')
    op.drop_index(op.f('ix_metakey_permission_key'), table_name='metakey_permission')
    op.drop_index(op.f('ix_metakey_permission_group_id'), table_name='metakey_permission')
    op.drop_table('metakey_permission')
    op.drop_index(op.f('ix_metakey_value'), table_name='metakey')
    op.drop_index(op.f('ix_metakey_key'), table_name='metakey')
    op.drop_table('metakey')
    op.drop_table('member')
    op.drop_index(op.f('ix_file_ssdeep'), table_name='file')
    op.drop_index(op.f('ix_file_sha512'), table_name='file')
    op.drop_index(op.f('ix_file_sha256'), table_name='file')
    op.drop_index(op.f('ix_file_sha1'), table_name='file')
    op.drop_index(op.f('ix_file_md5'), table_name='file')
    op.drop_index(op.f('ix_file_humanhash'), table_name='file')
    op.drop_index(op.f('ix_file_file_type'), table_name='file')
    op.drop_index(op.f('ix_file_file_size'), table_name='file')
    op.drop_index(op.f('ix_file_file_name'), table_name='file')
    op.drop_index(op.f('ix_file_crc32'), table_name='file')
    op.drop_table('file')
    op.drop_table('comment')
    op.drop_table('api_key')
    op.drop_index(op.f('ix_user_login'), table_name='user')
    op.drop_table('user')
    op.drop_index(op.f('ix_tag_tag'), table_name='tag')
    op.drop_table('tag')
    op.drop_index(op.f('ix_object_upload_time'), table_name='object')
    op.drop_index(op.f('ix_object_dhash'), table_name='object')
    op.drop_table('object')
    op.drop_table('metakey_definition')
    op.drop_index(op.f('ix_group_name'), table_name='group')
    op.drop_table('group')
    # ### end Alembic commands ###