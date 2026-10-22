---
title: "Функции: pkg/client"
type: functions
repo: kubernetes
language: ru
chunk_boundary: h3
group: pkg/client
---


# Функции: pkg/client


## Навигация


- [К оглавлению документации](../../README.md)

- [К индексу функций](../functions.md)

- [К разделам](../)

- [Предыдущая директория](pkg_certauthorization.md)

- [Следующая директория](pkg_controller.md)


---


## Меню по файлам


- 📄 [pkg/client/conditions/conditions.go](#pkgclientconditionsconditionsgo)


---


## pkg/client/conditions/conditions.go


📄 Исходный файл: `pkg/client/conditions/conditions.go`


<details open>
<summary><b>Функции в этом файле (2)</b></summary>


- 🔗 [PodCompleted](#podcompleted-pkgclientconditionsconditionsgo53) `:53`

- 🔗 [PodRunning](#podrunning-pkgclientconditionsconditionsgo34) `:34`


</details>


[function] name: PodCompleted file: pkg/client/conditions/conditions.go:53 returns_error: да description: PodCompleted returns true if the pod has run to completion, false if the pod has not yet
reached running state, or an er


### PodCompleted (pkg/client/conditions/conditions.go:53)


PodCompleted returns true if the pod has run to completion, false if the pod has not yet
reached running state, or an error in any other case.


```go
func PodCompleted((bool, error)) (bool, error)
```


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `bool`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `pkg/client/conditions/conditions.go:53`



---


[function] name: PodRunning file: pkg/client/conditions/conditions.go:34 returns_error: да description: PodRunning returns true if the pod is running, false if the pod has not yet reached running state,
returns ErrPodComplet


### PodRunning (pkg/client/conditions/conditions.go:34)


PodRunning returns true if the pod is running, false if the pod has not yet reached running state,
returns ErrPodCompleted if the pod has run to completion, or an error in any other case.


```go
func PodRunning((bool, error)) (bool, error)
```


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `bool`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `pkg/client/conditions/conditions.go:34`





---


## Навигация


- [К оглавлению документации](../../README.md)

- [К индексу функций](../functions.md)

- [К разделам](../)

- [Предыдущая директория](pkg_certauthorization.md)

- [Следующая директория](pkg_controller.md)


---

