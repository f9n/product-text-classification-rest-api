from fastapi import FastAPI, status, Body
from fastapi.responses import RedirectResponse
from fastapi.middleware.cors import CORSMiddleware

from scraper import Scraper

quotes = Scraper()

app = FastAPI(title="Product Text Classification Rest API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/", include_in_schema=False)
async def index():
    return RedirectResponse("/docs")


@app.get("/ping")
async def pong():
    return {"ping": "pong!"}


@app.get("/healthcheck", status_code=status.HTTP_200_OK)
def perform_healthcheck():
    """
    Simple route for the GitHub Actions to healthcheck on.
    More info is available at:
    https://github.com/akhileshns/heroku-deploy#health-check
    It basically sends a GET request to the route & hopes to get a "200"
    response code. Failing to return a 200 response code just enables
    the GitHub Actions to rollback to the last version the project was
    found in a "working condition". It acts as a last line of defense in
    case something goes south.
    Additionally, it also returns a JSON response in the form of:
    {
      'healtcheck': 'Everything OK!'
    }
    """
    return {"healthcheck": "Everything OK!"}


@app.get("/{text}")
async def read_item(text: str):
    print(text)
    return quotes.scrapedata(text)


@app.post("/classification")
async def classification_on_the_texts(texts: list[str] = Body(...)):
    print(texts)
    results = []
    for text in texts:
        result = quotes.scrapedata(text)
        results.append(result)

    return results
