resource "aws_lambda_function" "my_lambda" {
  filename = "${path.module}/Lambda/lambda_function.zip"
  function_name = var.lambda_function_name
  handler = "lambda_function.lambda_handler"
  runtime = "python3.8"
  source_code_hash = filebase64sha256("${path.module}/Lambda/lambda_function.zip")
  role = aws_iam_role.lambda_exec.arn
  depends_on = [aws_s3_bucket.my_bucket]
}