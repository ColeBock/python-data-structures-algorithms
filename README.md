# python-data-structures-algorithms

# Emergency Dispatch & Suburb Indexing System (Python)

Python implementations of core data structures and algorithms designed for **SafeRoute**, a municipal emergency-vehicle dispatch and route-reporting pilot system.

## Project Components

### 1. Emergency Incident Intake & Fleet Lookup (`emergency_dispatch_system.py`)
- **Min-Heap Priority Queue (`IncidentIntakeQueue`):** Uses Python's `heapq` module to prioritize `CRITICAL` incidents ahead of `ROUTINE` calls in $O(\log n)$ time while preserving strict FIFO arrival order within the same severity level.
- **Hash Table Vehicle Registry (`VehicleRegistry`):** Provides $O(1)$ average-time lookup of emergency vehicles and crew leads by registration number, complete with validation for empty queues, unknown registrations, and invalid severities.
- **Empirical Performance Benchmarking:** Compares Hash Table lookup speed against $O(n)$ linear list search across scaling fleet sizes:

| Dataset Size | Hash Table Lookup (ms) | Linear List Search (ms) |
| :--- | :--- | :--- |
| 5,000 records | 0.001500 ms | 0.215800 ms |
| 50,000 records | 0.002600 ms | 1.571100 ms |

### 2. Suburb Reporting & Indexing (`suburb_index_bst_hash.py`)
- **Hash Table & Binary Search Tree (BST):** Implements insertion and search operations across both structures for municipal suburb indexing.
- **In-Order BST Traversal:** Generates alphabetically sorted suburb listings in $O(n)$ time without requiring secondary sorting overhead.
- **Incident Frequency Tracker (`SimpleIncidentTracker`):** Tracks and retrieves real-time incident counts per suburb in $O(1)$ amortized time.

## How to Run
```bash
python emergency_dispatch_system.py
python suburb_index_bst_hash.py
