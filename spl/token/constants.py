"""SPL token constants."""

from safecoin.publickey import PublicKey

MINT_LEN: int = 82
"""Data length of a token mint account."""

ACCOUNT_LEN: int = 165
"""Data length of a token account."""

MULTISIG_LEN: int = 355
"""Data length of a multisig token account."""

ASSOCIATED_TOKEN_PROGRAM_ID = PublicKey("AToD9iqHSc2fhEP9Jp7UYA6mRjHQ4CTWyzCsw8X3tH7K")
"""Program ID for the associated token account program."""

TOKEN_PROGRAM_ID: PublicKey = PublicKey("ToKLx75MGim1d1jRusuVX8xvdvvbSDESVaNXpRA9PHN")
"""Public key that identifies the SPL token program."""

WRAPPED_SOL_MINT: PublicKey = PublicKey("Safe111111111111111111111111111111111111111")
"""Public key of the "Native Mint" for wrapping SAFE to SPL token.

The Token Program can be used to wrap native SOL. Doing so allows native SOL to be treated like any
other Token program token type and can be useful when being called from other programs that interact
with the Token Program's interface.
"""
