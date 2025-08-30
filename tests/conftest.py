from uuid import UUID
import pytest
import pytest_asyncio
from motor.motor_asyncio import AsyncIOMotorClient
from store.schemas.product import ProductIn
from tests.factories import product_data


@pytest_asyncio.fixture(scope="session")
async def mongo_client():
    client = AsyncIOMotorClient("mongodb://localhost:27017")
    yield client
    client.close()


@pytest_asyncio.fixture(autouse=True)
async def clear_collections(mongo_client):
    yield
    try:
        collections_names = await mongo_client.get_database().list_collection_names()
        for collection_name in collections_names:
            if collection_name.startswith("system"):
                continue

            await mongo_client.get_database()[collection_name].delete_many({})
    except Exception:
        pass


@pytest.fixture
def product_id() -> UUID:
    return UUID("ddc287ef-ab93-4ef5-8336-78883c422f6a")


@pytest.fixture
def product_in(product_id):
    return ProductIn(**product_data(), id=product_id)
