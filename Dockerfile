# Sử dụng Ubuntu 22.04 để hỗ trợ Python mới tốt hơn
# ------------------------------------------------------------
FROM nvidia/cuda:12.2.0-devel-ubuntu22.04
# ------------------------------------------------------------

ENV DEBIAN_FRONTEND=noninteractive

# Cài đặt Python 3.12 (hoặc 3.11 tùy bạn chọn)
# ------------------------------------------------------------
RUN apt-get update && apt-get install -y \
    software-properties-common \
    curl \
    git \
    && add-apt-repository -y ppa:deadsnakes/ppa \
    && apt-get update && apt-get install -y \
    python3.12 \
    python3.12-dev \
    python3.12-venv \
    && rm -rf /var/lib/apt/lists/*

# Cài đặt PIP cho Python 3.12
RUN curl -sS https://bootstrap.pypa.io/get-pip.py | python3.12

# Thiết lập Python 3.12 làm mặc định
RUN update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.12 1
RUN update-alternatives --install /usr/bin/python python /usr/bin/python3.12 1

WORKDIR /code
RUN mkdir -p /code/faiss_index
RUN python3 -m pip install --no-cache-dir gdown
RUN gdown --id 1S1gwz0sS7iwBv7ySDYJ0vjNixpz0bRYc -O /code/faiss_index/index.faiss
RUN gdown --id 1105pMnXBbY9MrPIuIIBJlBhvQbHiF5q_ -O /code/faiss_index/index.pkl
COPY . /code

# Dọn dẹp các file cache cũ của version khác để tránh xung đột
RUN find . -type d -name "__pycache__" -exec rm -rf {} +

# Cài đặt thư viện
RUN python3 -m pip install --no-cache-dir --upgrade pip setuptools wheel
RUN python3 -m pip install --no-cache-dir -r requirements.txt

RUN chmod +x inference.sh

CMD ["bash", "inference.sh"]