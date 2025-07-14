# Use official VSCode Ubuntu base image
FROM mcr.microsoft.com/vscode/devcontainers/base:ubuntu

# Install dependencies needed to build BCC and Python bindings
RUN apt-get update && apt-get install -y \
  bison build-essential cmake flex git libedit-dev \
  libllvm14 llvm-14-dev libclang-14-dev clang-14 \
  libelf-dev zlib1g-dev libfl-dev python3-setuptools python3-pip \
  liblzma-dev libzstd-dev libboost-dev \
  linux-headers-$(uname -r)

# Clone, build and install BCC
RUN git clone https://github.com/iovisor/bcc.git /tmp/bcc && \
  cd /tmp/bcc && mkdir build && cd build && \
  cmake .. -DCMAKE_INSTALL_PREFIX=/usr -DPYTHON_CMD=python3 -DENABLE_LLVM_NATIVECODEGEN=OFF && \
  make -j$(nproc) && make install

# Install BCC Python bindings
RUN pip3 install --upgrade pip && \
  cd /tmp/bcc/build/src/python/bcc-python3 && \
  pip3 install .

# Clean up build files and cache
RUN rm -rf /tmp/bcc && apt-get clean && rm -rf /var/lib/apt/lists/*

# Set working directory
WORKDIR /workspaces/ebpf-sandbox
