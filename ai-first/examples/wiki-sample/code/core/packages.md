---
title: core — пакеты
type: code-packages
components: [core]
repo: https://gitlab.example.com/mk8s/core
version: v1.2.0
commit: a0909767a3f9
generated: true
---

# core — пакеты

## pkg/cluster

`package cluster`

Package cluster описывает клиентский кластер платформы.

### Phase

`pkg/cluster/cluster.go:5` · type

Phase — фаза жизненного цикла кластера.

```go
type Phase string
```

### Cluster

`pkg/cluster/cluster.go:8` · type

Cluster — клиентский кластер.

```go
type Cluster struct {
	ID    string
	Phase Phase
}
```

### Cluster.Ready

`pkg/cluster/cluster.go:14` · method

Ready возвращает true, если кластер в фазе Running.

```go
func (c *Cluster) Ready() bool
```

### New

`pkg/cluster/cluster.go:17` · func

New создаёт кластер в фазе Pending.

```go
func New(id string) *Cluster
```

