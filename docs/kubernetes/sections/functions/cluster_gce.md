---
title: "Функции: cluster/gce"
type: functions
repo: kubernetes
language: ru
chunk_boundary: h3
group: cluster/gce
---


# Функции: cluster/gce


## Навигация


- [К оглавлению документации](../../README.md)

- [К индексу функций](../functions.md)

- [К разделам](../)

- [Предыдущая директория](build_pause.md)

- [Следующая директория](cluster_images.md)


---


## Меню по файлам


- 📄 [cluster/gce/gci/mounter/mounter.go](#clustergcegcimountermountergo)


---


## cluster/gce/gci/mounter/mounter.go


📄 Исходный файл: `cluster/gce/gci/mounter/mounter.go`


<details open>
<summary><b>Функции в этом файле (2)</b></summary>


- 🔗 [main](#main-clustergcegcimountermountergo38) `:38`

- 🔗 [mountInChroot](#mountinchroot-clustergcegcimountermountergo65) `:65`


</details>


[function] name: main file: cluster/gce/gci/mounter/mounter.go:38 returns_error: нет description: —


### main (cluster/gce/gci/mounter/mounter.go:38)


main is a function that performs operations based on the provided parameters and returns ().


```go
func main(()) ()
```


📍 *Расположение:* `cluster/gce/gci/mounter/mounter.go:38`



---


[function] name: mountInChroot file: cluster/gce/gci/mounter/mounter.go:65 returns_error: нет description: mountInChroot runs mount within chroot with the passing root directory


### mountInChroot (cluster/gce/gci/mounter/mounter.go:65)


mountInChroot runs mount within chroot with the passing root directory


```go
func mountInChroot((rootfsPath string, args []string)) (rootfsPath string, args []string)
```


**Тип ответа:** rootfsPath


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** args


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `cluster/gce/gci/mounter/mounter.go:65`





---


## Навигация


- [К оглавлению документации](../../README.md)

- [К индексу функций](../functions.md)

- [К разделам](../)

- [Предыдущая директория](build_pause.md)

- [Следующая директория](cluster_images.md)


---

