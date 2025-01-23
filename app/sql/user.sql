-- 認証済みユーザーのみがユーザーテーブルにデータを挿入できるようにする
CREATE POLICY "Allow insert for authenticated users"
ON "user"
FOR INSERT
WITH CHECK (auth.uid() = id);

