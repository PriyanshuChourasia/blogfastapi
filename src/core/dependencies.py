from typing import Annotated

from fastapi import Header, HTTPException

async def get_token_from_header(x_token: Annotated[str, Header()]):
    if x_token != 'Authorization':
        raise HTTPException(status_code=403, detail="Authorization invalid")