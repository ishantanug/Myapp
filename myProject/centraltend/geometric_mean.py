{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "15622589",
   "metadata": {
    "ExecuteTime": {
     "end_time": "2023-07-03T12:25:40.554168Z",
     "start_time": "2023-07-03T12:25:40.532171Z"
    }
   },
   "outputs": [],
   "source": [
    "import math\n",
    "\n",
    "def calculate_geometric_mean(numbers):\n",
    "    product = 1\n",
    "    for num in numbers:\n",
    "        product *= num\n",
    "    return math.pow(product, 1 / len(numbers))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": None,
   "id": "96573351",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.10"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
