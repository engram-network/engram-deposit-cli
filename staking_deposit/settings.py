from typing import Dict, NamedTuple
from eth_utils import decode_hex

DEPOSIT_CLI_VERSION = '2.5.0'


class BaseChainSetting(NamedTuple):
    NETWORK_NAME: str
    GENESIS_FORK_VERSION: bytes
    GENESIS_VALIDATORS_ROOT: bytes


MAINNET  = 'Mainnet'
GOERLI   = 'Goerli'
PRATER   = 'Prater'
SEPOLIA  = 'Sepolia'
ZHEJIANG = 'Zhejiang'
ENGRAM   = 'Engram'

# Mainnet setting
MainnetSetting = BaseChainSetting(
    NETWORK_NAME=MAINNET, GENESIS_FORK_VERSION=bytes.fromhex('00000000'),
    GENESIS_VALIDATORS_ROOT=bytes.fromhex('4b363db94e286120d76eb905340fdd4e54bfe9f06bf33ff6cf5ad27f511bfe95'))
# Goerli setting
GoerliSetting = BaseChainSetting(
    NETWORK_NAME=GOERLI, GENESIS_FORK_VERSION=bytes.fromhex('00001020'),
    GENESIS_VALIDATORS_ROOT=bytes.fromhex('043db0d9a83813551ee2f33450d23797757d430911a9320530ad8a0eabc43efb'))
# Sepolia setting
SepoliaSetting = BaseChainSetting(
    NETWORK_NAME=SEPOLIA, GENESIS_FORK_VERSION=bytes.fromhex('90000069'),
    GENESIS_VALIDATORS_ROOT=bytes.fromhex('d8ea171f3c94aea21ebc42a1ed61052acf3f9209c00e4efbaaddac09ed9b8078'))
# Zhejiang setting
ZhejiangSetting = BaseChainSetting(
    NETWORK_NAME=ZHEJIANG, GENESIS_FORK_VERSION=bytes.fromhex('00000069'),
    GENESIS_VALIDATORS_ROOT=bytes.fromhex('53a92d8f2bb1d85f62d16a156e6ebcd1bcaba652d0900b2c2f387826f3481f6f'))
# Engram setting
EngramSetting = BaseChainSetting(
    NETWORK_NAME=ENGRAM, GENESIS_FORK_VERSION=bytes.fromhex('10231196'),
    GENESIS_VALIDATORS_ROOT=bytes.fromhex('98837c9cdc462ae4cfb310f53800cc2c3638dfa4cbd16f06ee7dd71a60b09ca5')
)


ALL_CHAINS: Dict[str, BaseChainSetting] = {
    MAINNET: MainnetSetting,
    GOERLI: GoerliSetting,
    PRATER: GoerliSetting,  # Prater is the old name of the Prater/Goerli testnet
    SEPOLIA: SepoliaSetting,
    ZHEJIANG: ZhejiangSetting,
    ENGRAM: EngramSetting, # Engram is the testnet for the Merge (Eth2.0)
}


def get_chain_setting(chain_name: str = MAINNET) -> BaseChainSetting:
    return ALL_CHAINS[chain_name]


def get_devnet_chain_setting(network_name: str,
                             genesis_fork_version: str,
                             genesis_validator_root: str) -> BaseChainSetting:
    return BaseChainSetting(
        NETWORK_NAME=network_name,
        GENESIS_FORK_VERSION=decode_hex(genesis_fork_version),
        GENESIS_VALIDATORS_ROOT=decode_hex(genesis_validator_root),
    )