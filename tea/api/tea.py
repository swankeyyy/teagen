from fastapi import APIRouter

router = APIRouter()

fake_tea = [{'name': 'puer', 'recipe': 'asd'}, {'name': 'puer', 'recipe': 'asd'}, {'name': 'puer', 'recipe': 'asd'},
            {'name': 'puer',
             'recipe': 'asd'}]


@router.get("/")
async def root():
    return fake_tea
