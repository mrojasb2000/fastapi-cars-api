from fastapi import APIRouter, HTTPException, status, Path
from models.account_type import AccountType

accounts_router = APIRouter(tags=["Accounts"])


@accounts_router.get("/{acc_type}/{months}")
async def account(acc_type: AccountType, months: int = Path(..., ge=3,le=12)):
    return {"message": "Account created", "account_type": acc_type, "months": months}