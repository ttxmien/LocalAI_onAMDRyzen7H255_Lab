# Script thiết lập biến môi trường tối ưu cho AMD Radeon 780M (ThinkBook 14 G8+)
Write-Host "=== Đang cấu hình biến môi trường Local AI cho AMD Radeon 780M ===" -ForegroundColor Cyan

$envVars = @{
    "OLLAMA_VULKAN" = "1"
    "OLLAMA_FLASH_ATTENTION" = "1"
    "OLLAMA_KV_CACHE_TYPE" = "q8_0"
    "OLLAMA_MAX_LOADED_MODELS" = "1"
    "OLLAMA_NUM_PARALLEL" = "2"
}

foreach ($key in $envVars.Keys) {
    $val = $envVars[$key]
    [System.Environment]::SetEnvironmentVariable($key, $val, [System.EnvironmentVariableTarget]::User)
    Write-Host "[OK] Set $key = $val" -ForegroundColor Green
}

Write-Host "`nHoàn tất! Vui lòng khởi động lại Ollama hoặc mở Terminal mới để áp dụng cấu hình." -ForegroundColor Yellow
