# 📦 SmartOrders – Resilient Microservices E-commerce System

SmartOrders is a containerized, fault-tolerant microservices-based **e-commerce platform prototype**. It showcases robust service-to-service communication, dynamic circuit breaker logic, and system resilience using Docker and Python (Flask).

---

## 🚀 What This Project Does

SmartOrders simulates a small e-commerce system that:

- Registers users
- Places product orders
- Handles (mocked) payments
- Checks inventory stock
- Protects itself from service failures via **circuit breakers**

Each feature is handled by an isolated microservice that can be monitored, scaled, and tested independently.

---

## 🧰 Tech Stack

- **Python (Flask)** – Each microservice backend
- **MongoDB / PostgreSQL** – Data storage
- **Docker & Docker Compose** – Containerization and orchestration
- **REST APIs** – Communication between services
- **Custom Circuit Breaker Logic** – Failure handling in `order-service`
- **Prometheus + Grafana (optional)** – Metrics and monitoring

---

## 🧱 Microservices Breakdown

| Service             | Description                                          | Port  |
|---------------------|------------------------------------------------------|-------|
| `user-service`      | User registration and login                         | 5001  |
| `order-service`     | Places orders, calls payment/inventory services     | 5002  |
| `inventory-service` | Checks product availability                         | 5003  |
| `payment-service`   | Simulates payments, supports failure simulation     | 5004  |
| `gateway`           | Routes external traffic to internal services (TODO) | 5000  |

---

## 🛠 How It Works

When a user places an order:

1. `order-service` receives the order request.
2. It verifies the user via `user-service`.
3. It checks stock via `inventory-service`.
4. It processes the payment via `payment-service`.

If inventory or payment fails 3 times in a row, the circuit breaker:
- **Opens the circuit**
- **Pauses further requests** to that service for 10 seconds
- **Prevents cascading failure**

---

## 📂 Project Structure

```
smartorders/
├── docker-compose.yml
├── user-service/
├── order-service/
├── inventory-service/
├── payment-service/
├── gateway/ (optional)
├── shared/
```

---

## 🧪 Sample API Request

Place an order via `order-service`:

```bash
curl -X POST http://localhost:5002/place-order \
  -H "Content-Type: application/json" \
  -d '{"user_id": "1", "item_id": "item1"}'
```

---

## 🧪 Swagger UI

Each service can expose its API using Swagger UI:

1. Install `flasgger`:
   ```bash
   pip install flasgger
   ```
2. Add to `app.py`:
   ```python
   from flasgger import Swagger
   Swagger(app)
   ```
3. Visit:  
   `http://localhost:5001/apidocs` – User API  
   `http://localhost:5002/apidocs` – Order API  
   *(Repeat for other services)*

---

## 🐳 Docker Setup

To run everything:

```bash
git clone https://github.com/your-username/smartorders.git
cd smartorders
docker compose up --build
```

Visit:  
- `http://localhost:5001/` – User Service  
- `http://localhost:5002/` – Order Service  
- etc.

---

## 📊 Future Enhancements

- Add API Gateway (Nginx or Flask proxy)
- Deploy monitoring stack (Prometheus + Grafana)
- Add JWT authentication
- Implement retry logic and exponential backoff

---

## 🎯 Learning Objectives

✅ Microservices Architecture  
✅ Docker & Service Isolation  
✅ Circuit Breaker Pattern  
✅ RESTful API Design  
✅ Scalable & Fault-Tolerant Systems

---

## 📄 License

MIT License

---

Made with 💡 by [Ignacio Deleon](https://github.com/ignaciod25)
