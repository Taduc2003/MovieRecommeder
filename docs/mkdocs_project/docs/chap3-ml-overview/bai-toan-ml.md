# Bài toán Machine Learning của project

## Định nghĩa bài toán

**Bài toán:** Dự đoán xếp hạng phim (rating prediction) cho người dùng dựa trên lịch sử xếp hạng của các người dùng khác (Collaborative Filtering).

**Loại bài toán:** Regression/Recommendation

## Công thức toán học

Với user u và item (phim) i, mục tiêu là dự đoán rating $\hat{r}_{ui}$

Sử dụng matrix factorization:

$$\hat{r}_{ui} = p_u \cdot q_i^T$$

Trong đó:
- $p_u$: latent factors của user u
- $q_i$: latent factors của item i

## Ứng dụng thực tế

Cung cấp gợi ý phim được cá nhân hóa cho người dùng, giúp họ khám phá những bộ phim mà họ có thể thích dựa trên sở thích của những người dùng tương tự.

## Ví dụ minh họa

Giả sử:
- User A đã xếp hạo: "Inception" (5), "Dark Knight" (4.5), "Interstellar" (5)
- User B đã xếp hạo: "Inception" (4.5), "Dark Knight" (5), "Interstellar" (4), "Pulp Fiction" (5)
- User C chưa xếp hạo "Pulp Fiction"

Collaborative Filtering sẽ dự đoán: User C sẽ thích "Pulp Fiction" vì C có sở thích tương tự A & B
