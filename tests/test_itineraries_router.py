import unittest
from fastapi.testclient import TestClient
from init import app

client = TestClient(app)


class TestItinerariesRouter(unittest.TestCase):

    def test_get_airports_success(self):
        # Datos de prueba
        payload = {
            "origin": 1,
            "destination": 6
        }
        response = client.post("/itineraries/", json=payload)
        self.assertEqual(response.status_code, 200)

        # Verificar que la respuesta sea una lista de itinerarios
        data = response.json()['data']
        self.assertIsInstance(data, list)
        if data:
            self.assertIn("itinerary_id", data[0])
            self.assertIn("origin", data[0])
            self.assertIn("destination", data[0])
            self.assertIn("total_duration", data[0])
            self.assertIn("route", data[0])
            self.assertIn("segments", data[0])

    def test_get_airports_no_itineraries_found(self):
        # Datos de prueba con un origen y destino que no existen
        payload = {
            "origin": 999,
            "destination": 999
        }
        response = client.post("/itineraries/", json=payload)
        self.assertEqual(response.status_code, 200)

        # Verificar que la respuesta sea una lista vacía
        data = response.json()['data']
        self.assertIsInstance(data, list)
        self.assertEqual(len(data), 0)


if __name__ == "__main__":
    unittest.main()
